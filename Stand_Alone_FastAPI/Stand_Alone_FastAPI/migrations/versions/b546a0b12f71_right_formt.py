"""right_formt

Revision ID: b546a0b12f71
Revises: d2faa3708112
Create Date: 2023-09-24 12:41:56.782760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b546a0b12f71'
down_revision: Union[str, None] = 'd2faa3708112'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('academicSessions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('academicSessions',
    sa.Column('sourcedId', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('status', postgresql.ENUM('active', 'tobedeleted', 'inactive', name='enum1'), autoincrement=False, nullable=False),
    sa.Column('dateLastModified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('type', postgresql.ENUM('gradingPeriod', 'semester', 'schoolYear', 'term', name='enum2'), autoincrement=False, nullable=False),
    sa.Column('startDate', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('EndDate', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('parentSourcedId', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('SchoolYear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('sourcedId', 'parentSourcedId', name='academicSessions_pkey'),
    sa.UniqueConstraint('parentSourcedId', name='academicSessions_parentSourcedId_key'),
    sa.UniqueConstraint('sourcedId', name='academicSessions_sourcedId_key')
    )
    # ### end Alembic commands ###
